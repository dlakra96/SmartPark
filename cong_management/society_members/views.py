from django.db.models.fields import return_None
from django.http import HttpResponse
from twilio.rest import Client
from django.template import loader
from .models import members
from django import template
from django.conf import settings
from django.shortcuts import get_object_or_404,render
import os

import cv2

import DetectChars
import DetectPlates
import PossiblePlate

def index(request):
    all_members = members.objects.all()
    template = loader.get_template('society_members/FrontPage.html')
    context = {
        'all_members': all_members,
    }
    return HttpResponse(template.render(context, request))

def number_search(request):

    flag=False

    mobile_no=""
    car_no="TN176000"
    all_members = members.objects.all()
    for m in all_members:
        if(m.car_number==car_no):
            mobile_no=m.mobile_number
            flag=True
            break
    if flag==False:
        return HttpResponse("<p style='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>No mobile number present in the database</p>")
    else:
        account_sid = "ACc232c3ba5ef74fd4317e5541f32a1560"
        auth_token = "117e21868ac9f3b1f0aa4358299e78f1"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+91"+str(mobile_no)+"",
            from_="+12055881778",
            body="Your Car is in Queue....")
        return HttpResponse("<p style='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>Message sent to the concerned user</p>")


def detail(request,members_id):
    return HttpResponse("<h2> Details for Car Number is :"+str(members.id)+"</h2>")
def manage_other(request):
        all_members = members.objects.all()

        context = {
            'all_members': all_members,
            }

        if(request.method=="POST"):
            SCALAR_BLACK = (0.0, 0.0, 0.0)
            SCALAR_WHITE = (255.0, 255.0, 255.0)
            SCALAR_YELLOW = (0.0, 255.0, 255.0)
            SCALAR_GREEN = (0.0, 255.0, 0.0)
            SCALAR_RED = (0.0, 0.0, 255.0)
            showSteps = False
            image = request.GET.get("img")
            def main():

                blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()  # attempt KNN training

                if blnKNNTrainingSuccessful == False:  # if KNN training was not successful

                    return HttpResponse("<pstyle='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>error: KNN traning was not successful</p>")  # and exit program
                # end if

                imgOriginalScene = cv2.imread(image)
                # open image

                if imgOriginalScene is None:  # if image was not read successfully
                    return HttpResponse("<pstyle='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>error: image not read from file</p>")  # and exit program
                # end if

                listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)  # detect plates

                listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)  # detect chars in plates


                if len(listOfPossiblePlates) == 0:  # if no plates were found
                    msg="\nno license plates were detected\n"  # inform user no plates were found
                else:  # else
                    # if we get in here list of possible plates has at leat one plate

                    # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
                    listOfPossiblePlates.sort(key=lambda possiblePlate: len(possiblePlate.strChars), reverse=True)

                    # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
                    licPlate = listOfPossiblePlates[0]


                    if len(licPlate.strChars) == 0:  # if no chars were found in the plate

                        return HttpResponse("<pstyle='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>no characters were detected</p>")
                    # end if





                return HttpResponse("<pstyle='color:red;font-size:20px;font-family:tahoma,times,calibri;padding-left:500px;padding-top:40px;background-color:cyan;'>Matched Car Number is" + licPlate.strChars + "</p>")
            if __name__ == "__main__":
                main()
        else:
            return render(request,'society_members/FrontPage.html',context)

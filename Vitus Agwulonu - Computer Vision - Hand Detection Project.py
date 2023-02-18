#!/usr/bin/env python
# coding: utf-8

# ### Vitus Hand Detection Project

# In[1]:


get_ipython().system('pip install mediapipe')


# In[2]:


# Step 1: Import all necessary libaries

import cv2
import mediapipe as mp


# In[3]:


# Step2: Identify your webcam

cap = cv2.VideoCapture(0) # local webcam - 0, External webcam - 1


# In[4]:


# Step 4: Leveraging the Mediapipe library used for hand detection

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# In[5]:


# Step 3: switch on webcam

while True:
    _, img = cap.read()
    
    #convert image from BG to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #Apply mediapipe
    results = hands.process(imgRGB)
    
    #print(results.multi_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
    
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.putText(img, "Vitus Hand Detection Project", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv2.imshow("Vitus Hand Detection Project", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture once all the processing is done.
cap.release()
cv2.destroyAllWindows()


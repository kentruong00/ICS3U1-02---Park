hour = int(input())
minute = int(input())
hourAngle = hour*30 + 30*(minute/60)
minuteAngle = 360 * (minute/60)
diff = max(hourAngle,minuteAngle) - min(hourAngle,minuteAngle)
print(diff)
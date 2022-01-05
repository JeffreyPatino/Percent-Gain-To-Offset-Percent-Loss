x = 1000
percentChange = int(input("Enter current percent change (without a % sign) in asset (put a negative (-) in front if a loss): "))
if percentChange < 0:
    percentChange = -percentChange
    percentChangeAsADecimal = percentChange / 100
    valueAfter = x * (1-percentChangeAsADecimal)
    finalAnswer = ((x / valueAfter) - 1) * 100
    print(round(finalAnswer,2), "%", sep='')
    print("You need a " + str(round(finalAnswer,2)) + "% gain to offset your " + str(percentChange) + "% loss" )
else:
    percentChangeAsADecimal = percentChange / 100
    valueAfter = x * (1+percentChangeAsADecimal)
    finalAnswer = ((x / valueAfter) - 1) * 100
    print(round(finalAnswer,2), "%", sep='')
    print("You need a " + str(round(-finalAnswer,2)) + "% loss to offset your " + str(percentChange) + "% gain" )

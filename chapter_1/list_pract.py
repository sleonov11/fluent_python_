"""
Чтобы быстро построить последовательность, можно воспользоваться списко-
вым включением (если конечная последовательность – список) или генера-
торным выражением (для всех прочих типов последовательностей). Если вы
не пользуетесь этими средствами в повседневной работе, клянусь, вы упускае-
те возможность писать код, который одновременно является и более быстрым,
и более удобочитаемым.
"""
"""
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes_1 = [ord(symbol) for symbol in symbols]
print(codes_1)

"""

colors = ['white', 'black']
sizes = ['s', 'm', 'l', 'xl']
shirts = [(color, size) for color in colors for size in sizes]
print(shirts)

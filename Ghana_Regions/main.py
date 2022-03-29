import turtle as t
import pandas

# Setting up the screen
screen = t.Screen()
screen.title("Ghana's 16 Regions")
image = "Ghana_Regions.gif"
t.addshape(image)
t.shape(image)

regions = []
correct_guesses = []

continue_game = True


# Scores based on the number of correct guesses
def score_fun():
    score = len(correct_guesses)
    return str(score) + "/16 regions guessed"


# print(answer_region)
region_data = pandas.read_csv("16_regions.csv")

data_dict = region_data.to_dict()

# print(data_dict)


for x in range(16):
    region = data_dict["region"][x]
    # print(region)
    regions.append(region)

# if user enters exit, a csv file of unprovided regions is created. 
while continue_game:
    answer_region = screen.textinput(title=f"{score_fun()}", prompt="What's another region's name").title()
    if answer_region == "Exit":
        remaining_regions = []
        regions_left = [remaining_regions.append(state) for state in regions if state not in correct_guesses]
        missing_answers = pandas.DataFrame(remaining_regions)
        missing_answers.to_csv("./Regions_You_Need_to_know")
        break
        # print(remaining_regions)

# If user gives a correct answer. it is added to correct guesses and written on the map.
    if answer_region in regions:
        state_x = int(region_data[region_data.region == answer_region]['x'])
        state_y = int(region_data[region_data.region == answer_region]['y'])
        tilly = t.Turtle()
        tilly.hideturtle()
        tilly.penup()
        tilly.goto(state_x, state_y)
        tilly.write(answer_region)
        correct_guesses.append(answer_region)
        if len(correct_guesses) == 16:
            continue_game = False





# Getting mouse click coordinates needed for the game.
#
# def click_coor(x, y):
#     print(x, y)
#
#
# t.onscreenclick(click_coor)
# t.mainloop()

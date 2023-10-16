import matplotlib.pyplot as plt
 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
video_game_hours = [1, 2, 2, 1, 2]
book_hours = [2, 3, 4, 2, 1]
 
plt.bar(range(len(video_game_hours)),video_game_hours) 
plt.bar(range(len(book_hours)),book_hours, bottom=video_game_hours)
plt.xticks(ticks = [0,1,2,3,4], labels = days)
plt.legend(["Video Games", "Books"])
plt.title("Breakdown of Entertainment Hours")
plt.show()
 
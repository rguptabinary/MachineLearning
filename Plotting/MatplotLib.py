import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

if(False):
    plt.plot([1, 2, 3], [5, 7, 4])

    plt.show()

# 2. Legends, title and labels
# https://www.youtube.com/watch?v=aCULcv_IQYw&index=2&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

if(False):
    x = [1,2,3]
    y = [5,7,4]

    x2 = [1, 2, 3]
    y2 = [10, 14, 12]

    plt.plot(x, y, label='First line') # plotting with legend
    plt.plot(x2, y2, label='Second line')

    plt.xlabel('plot number')
    plt.ylabel('important var')
    plt.title('Interesting graph\nCheck it out') # with subtitles
    plt.legend() # Show legends
    plt.show()

# 3. Bar charts and Histogram
# https://www.youtube.com/watch?v=ZyTO4SwhSeE&index=3&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

# Bar graph
if(False):
    x = [2, 4, 6, 8, 10]
    y = [6, 7, 8, 2, 4]

    x2 = [1, 3, 5, 9, 10]
    y2 = [7, 8, 2, 4, 2]

    plt.bar(x, y, label='Bar1', color='b')
    plt.bar(x2, y2, label='Bar2', color='c')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting graph')
    plt.legend()

    plt.show()

# Histograms
# To better understand the distributions
if(False):
    population_ages = [33,12,34,54,12,54,111,45,64,76,67,89,98,88,76,56,54,44,99,111,123,43]
    # ids = [x for x in range(len(population_ages))]

    # plt.bar(ids, population_ages)

    # Histogram has bins (elements containing stuffs)
    bins = [i for i in range(0, 130, 10)]

    plt.hist(population_ages, bins, histtype='bar', rwidth=0.9)

    plt.show()

# 4. Scatter plots
# https://www.youtube.com/watch?v=WbTOutpwPHs&index=4&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

if(False):
    x = [1,2,3,4,5,6,7,8]
    y = [4,3,2,5,3,7,9,2]

    plt.scatter(x, y, label='Scatter plot', color='r', marker='o', s=200)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersting graph')

    plt.legend()
    plt.show()

# 5. Stack plots
# https://www.youtube.com/watch?v=Z81JW1NTsO8&index=5&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

if(False):
    days = [1, 2, 3, 4, 5]
    
    sleeping = [7, 8, 6, 10, 5]
    eating   = [2, 3, 4, 3, 2]
    working  = [7, 8, 7, 2, 4]
    playing  = [8, 5, 7, 8, 13]

    # No way to define labels
    plt.stackplot(days, sleeping, eating, working, playing, colors=['r', 'b', 'c', 'g'])

    # Tricks to define labels
    plt.plot([], [], color='r', label='sleeping', linewidth=5)
    plt.plot([], [], color='b', label='eating', linewidth=5)
    plt.plot([], [], color='c', label='working', linewidth=5)
    plt.plot([], [], color='g', label='playing', linewidth=5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting graph')
    plt.legend()

    plt.show()

# 6. Pi charts
# https://www.youtube.com/watch?v=Oh2Dkkswy30&index=6&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

if(False):
    days = [1, 2, 3, 4, 5]
    
    sleeping = [7, 8, 6, 10, 5]
    eating   = [2, 3, 4, 3, 2]
    working  = [7, 8, 7, 2, 4]
    playing  = [8, 5, 7, 8, 13]

    slices = [5, 2, 4, 13]
    activities = ['sleeping', 'eating', 'working', 'playing']
    cols = ['c', 'm', 'r', 'y']

    plt.pie(slices, 
            labels=activities, 
            colors=cols, 
            startangle=90, 
            shadow=True,
            explode=[0, .1, 0, 0],
            autopct='%1.1f%%')

    plt.show()

# 7. Getting data from the files
# https://www.youtube.com/watch?v=QyhqzaMiFxk&index=7&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF
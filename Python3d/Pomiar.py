from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import pickle
import os


class Pomiar:

    def __init__(self, mes_title, mes_num):
        self.points_list = []
        self.x_list = []
        self.y_list = []
        self.z_list = []
        self.mes_title = mes_title
        self.mes_num = mes_num

    def add_point(self, point):
        self.points_list.append(point)

    def calculate_all(self):
        self.x_list = []
        self.y_list = []
        self.z_list = []

        for point in self.points_list:
            x, y, z = point.calculate()
            self.x_list.append(x)
            self.y_list.append(y)
            self.z_list.append(z)

        return (self.x_list, self.y_list, self.z_list)

    def clear(self):
        self.points_list = []
        self.x_list = []
        self.y_list = []
        self.z_list = []

    def display_plot(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        # Data for three-dimensional scattered points
        ax.scatter3D(self.x_list, self.y_list,
                     self.z_list, c='r', cmap='OrRd_r')
        ax.set_xlabel('x axis')
        ax.set_ylabel('y axis')
        ax.set_zlabel('z axis')
        plt.title(self.mes_title)
        plt.show()

    def print_info(self):
        print("Pomiar title = " + str(self.mes_title))
        print("number of measurements = " + str(len(self.points_list)))

    def save_pickle(self, filename):
        filehandler = open(filename, 'wb')
        pickle.dump(self, filehandler)

    def save_with_title(self, path):
        self.save_pickle(os.path.join(path, self.mes_title + ".obj"))

    @staticmethod
    def load_pickle(filename):
        filehandler = open(filename, 'rb')
        return pickle.load(filehandler)

import numpy as np
import matplotlib.pyplot as plt

class Gale_Sharply:
    def __init__(self, wpreff, mpreff):  
        """
        Initializes the Gale_Sharply class with two preference matrices.

        Args:
        wpreff (numpy.ndarray): A 2D numpy array representing the women's preference matrix.
        mpreff (numpy.ndarray): A 2D numpy array representing the men's preference matrix.
        """
        self.wpref = wpreff
        self.mpref = mpreff
        self.N = len(wpreff)
        self.wpre = [] 
        self.mpre = []

        for i in range(N):
            temp1 = [i for i in range(N)]
            temp2 = [i for i in range(N)]
            zipped_1 = sorted(zip(self.wpref[i],temp1),reverse=True)
            zipped_2 = sorted(zip(self.mpref[i],temp2),reverse=True)
            temp1_sorted = [t[1] for t in zipped_1]
            temp2_sorted = [t[1] for t in zipped_2]
            self.wpre.append(temp1_sorted)
            self.mpre.append(temp2_sorted)
        
    def drawPreferenceTable(self):
        """
        Draws the preference table for both men and women.
        """
        fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,10))

        ax1.set_title('Women Preference Table')
        im1 = ax1.imshow(wpref1,  interpolation='nearest', cmap='Blues')
        plt.colorbar(im1, ax=ax1)

        ax2.set_title('Man Preference Table')
        im2 = ax2.imshow(mpref1,  interpolation='nearest', cmap='Oranges')
        plt.colorbar(im2, ax=ax2)


        plt.show()

    
    def drawRankingTable(self):
        """
        Draws the RankingTable for both men and women.
        """
        fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,10))

        ax1.set_title('Women Preference List')
        im1 = ax1.imshow(self.wpref,cmap = 'cool')
       

        ax2.set_title('Man Preference List')
        im2 = ax2.imshow(self.mpref ,cmap= 'cool')
        for i in range(self.N):
            for j in range(self.N):
                text1 = ax1.text(j, i, self.wpref[i][j],
                            ha="center", va="center", color="w")
                text2 = ax2.text(j, i, self.mpref[i][j],
                            ha="center", va="center", color="w")
        plt.show()
        
                
N = 5   
np.random.seed(3)
wpref1 = np.random.rand(N,N)
mpref1 = np.random.rand(N,N)
gs = Gale_Sharply(wpref1,mpref1)
gs.drawRankingTable()

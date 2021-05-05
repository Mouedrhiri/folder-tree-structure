# Get Folder (Paths , Sub-directories , Files) Tree Structure By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

### The I Used The Library Imaplib To Give Me Acces To Gmail Account

`import imaplib`

### I've Made a Function For The Progress Bar Like That :

    def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

> As You All Can See I Made This Progress Bar Relative To The Searching Progress

---

# Let's Begin The Code Explanation :

## I've Started With Getting The Folder Directory Using Simple Input :

`folder = input("Enter The Folder Path : ")`

## And Then Start Looping In The Folder Paths and Files Using Simple For Loop With Folders Parameteres :

### So Here We Are Getting The Path and Sub directories and Files From OS :

    for path, subdirs, files in os.walk(rf'{folder}'):

### Here Importing The Progress Bar with FPath As A Parametre :

    progress(path)

### Here I'm Getting The Name Files And Directories

    for name in files:

### As Far As We All Know That Os Give us the path and The Name in a separated Way So We Need To Combine Them Using Join Function :

    print(os.path.join(path, name))

---

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)

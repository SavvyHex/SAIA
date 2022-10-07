# SAIA
![](https://i.imgur.com/7LA6HHO.png)
SAIA is a command line tool used for a variety of tasks. It is a one-file made using multiple packages and APIs, with click being the most used.

## Commands :
### bino :
Returns the binomial formula for (a+b)ⁿ

It requires only one argument :
- ROW_NUMBER : The power to which (a+b) has to be raised.

For Example :
![](https://i.imgur.com/A8kzj2T.png)

### calc :
Evaluates a simple mathematical expression, as how you would type it in python. Please note that the numbers and signs should not be seperated by spaces.

For Example :

![](https://i.imgur.com/ZeJ4nuc.png)

### comb :
Gives you the possible combinations for a set of articles using the formula :

![](https://i.imgur.com/GpGJZUo.png)

It requires two arguments :
- N : Total number of articles
- R : Number of articles required per combination

For Example :

![](https://i.imgur.com/MSexadT.png)

### element :
Using the [periodic table](https://pypi.org/project/periodictable/) module, this command will give you basic information about an element.

It accepts three options out of which only **one** should be entered :
- --num : The atomic number of the element
- --sym : The symbol of the element (case sensitive)
- --name : The name of the element (case insensitive)

If all three options are left blank, information of a random element will be displayed.

Information of the element that will be displayed :
- Atomic Number of the element
- Name of the element
- Symbol of the element
- Atomic Mass of the element
- Density of the element

For Example :

![](https://i.imgur.com/FW9l5cW.png)

### perm :
Gives you the possible permutations for a set of articles using the formula :

![](https://i.imgur.com/wjfiQe7.png)

It requires two arguments :
- N : Total number of articles
- R : Number of articles required per permutation

For Example :

![](https://i.imgur.com/OGMnb0x.png)

### ptr :
This command returns all of the numbers present in a specified row of the Pascal's Triangle. Please note that row number 0 is the first row of the triangle.

It requires only one argument :
- ROW_NUMBER : The row of the triangle

For Example :

![](https://i.imgur.com/EyROC28.png)
### trig :
It returns the value of the trignometric ratio for a specified angle. Please note that the angle should be in degrees.

It requires only one argument :
- VALUE : The angle, in degrees

It has six subcommands, one for each trignometric function :
- sin
- cos
- tan
- cot
- sec
- cosec
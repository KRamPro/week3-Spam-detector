## Experiment 1

Using the spiral dataset, a learning rate of 0.001, a Tanh activation, and zero hidden layers, there was a little progress at the beginning, but it quickly stopped. With one layer there was a bit more progress, but it still didn't seem to learn.

With one hidden layer and eight neurons, it kept learning, but pretty slowly: the loss went from 0.500 to 0.333 at 2,000 epochs. With two layers and eight neurons, it made progress slowly for quite a while, but got a little past the other loss rating, reaching 0.325.

![Pasted image 20261108201809.png](images/Pasted%20image%2020261108201809.png)

Hidden layers with nonlinear activations can combine simpler patterns into more flexible boundaries. My screenshot shows the circle dataset, so I still need to test the spiral.

## Experiment 2

I wasn't able to make a huge difference using Linear on this three-layer setup that learned before.

![Pasted image 20261108202549.png](images/Pasted%20image%2020261108202549.png)

The loss sank a little, but then seemed to get stuck around 0.496 with Linear.

![Pasted image 20261108202637.png](images/Pasted%20image%2020261108202637.png)

It also stopped at 0.496 with six hidden layers, which confused me. Why didn't all that extra room help it learn?

Stacking linear layers still produces a linear transformation. More layers alone can't create the curved boundary needed for the spiral.

![Pasted image 20261108202813.png](images/Pasted%20image%2020261108202813.png)

## Experiment 3

I took the default configuration again and subjected it to a really high and a really low learning rate.

![Pasted image 20261108202937.png](images/Pasted%20image%2020261108202937.png)

In the default state it learned really fast.

![Pasted image 20261108203030.png](images/Pasted%20image%2020261108203030.png)

At the low rate, the loss sank a little, but didn't make enough progress even after 3,000 epochs.

![Pasted image 20261108203146.png](images/Pasted%20image%2020261108203146.png)

At a learning rate of 10, the system radically overcorrected and the loss shot up! At 0.00001, the weight changes were too small to make much progress.

## Experiment 4

With the noise at 50, I noticed some progress really quickly, then it kinda slowed down before the loss sank again. It finally leveled off.

![Pasted image 20261108203415.png](images/Pasted%20image%2020261108203415.png)

The boundary is roughly a blue center surrounded by orange, with some uneven edges. The network could start fitting random noisy points instead of the general pattern.

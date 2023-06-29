import tensorflow as tf
import numpy as np
import matplotlib as plt

def f(x):
    return x**4-3*x**3+2
def fprime(x):
    h=0.001
    return (f(x+h)-f(x))/h

k=0
max_iters = 1000
lr = 0.001
tol = 1e-5

x_old = 0.0
x_new = 4.0
x_list = [x_new]
x = tf.Variable(x_new, dtype=tf.float32)

while abs(x_old - x_new) > tol and k < max_iters:
    k+=1
    x_old = x.numpy()
    step=lr*fprime(x)
    x.assign_sub(step, read_value = False)
    x_new = x.numpy()
    x_list.append(x_new)
print('k={}:f({})={}'.format(k, x_new,f(x_new)))

print("[f(0),f(9/4),f(-2),f(4)]=",[f(0),f(9/4),f(-2),f(4)])

xs = tf.linspace(-2.0, 4.0, num=101)
ys = f(xs)
plt.plot(xs,ys,'b-')

x_list = tf.constant(x_list, dtype=tf.float32)
y_list = f(x_list)
plt.plot(x_list, y_list,'ro')
plt.show()
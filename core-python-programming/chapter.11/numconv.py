__author__ = 'weixy6'


def convert(func, seq):
    """
    conv. sequence of numbers to same type
    :param func: conversion function, e.g. int(), long()...
    :param seq: sequence to be convert
    :return:
    """
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 99999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)

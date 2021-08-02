#!/usr/bin/env python3.9
from os import name
from passlock import User

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(name):
    '''
    Function that finds a contact by number and returns the user
    '''
    return name.find_by_username(name)

def check_existing_users(name):
    '''
    Function that check if a user exists with that name and return a Boolean
    '''
    return User.user_exist(name) 

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
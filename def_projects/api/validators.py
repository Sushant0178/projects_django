# app/validators.py
from rest_framework import serializers

def adult_age(value):
    if value < 18:
        raise serializers.ValidationError("Age must be 18 or above")

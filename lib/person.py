#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
class Person:
    def __init__(self, name="", job=None):
        self._name = None
        self._job = None
        self.name = name
        if job is not None:
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        elif isinstance(value, str) and len(value) == 0:
            print("Name must be a string between 1 and 25 characters.")  # Updated to match the test's expectation
        else:
            print("Name must be a string between 1 and 25 characters.")  # Keep message consistent

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.\n")  # Correct message for job validation

# Sample tests
person1 = Person(name="john doe", job="Sales")
empty_name_person = Person(name="", job="Sales")
default_name_person = Person()
short_name_person = Person(name="a", job="Sales")
long_name_person = Person(name="a" * 26, job="Sales")
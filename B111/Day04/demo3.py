#rules to specify variable name
#1. no keywords
number=100 #valid example
#lambda=200 #invalid example

#2. can contain only a-z A-Z 0-9 _ (not allowed-->space and other special char)
emp1='bhanu' #valid example
# emp name='bhanu' #invalid example
# amount$=300 #invalid example

#3. it cant start with digit (it can start with a-z A-Z _)
emp_1='bhanu' #valid example
MyName='bhanu' #valid example
_emp='vijay'  #valid example
__emp='ravi'  #valid example
# 1emp='bhanu' #invalid example

#4 it is case sensitive
emp='surya'
emp='bhanu'
EMP='ravi'
print(emp,'<-small case')
print(EMP,'capital , case sensitive')

#5 no max limit
this_is_my_variable_which_i_created_for_time_pass=10
print(this_is_my_variable_which_i_created_for_time_pass,'max length variable')





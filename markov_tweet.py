
import tweepy, random

def read_api_keys():
	file = open('.api_keys.txt')
	api_keys_dict = {}
		     
	
	for each_line in file:
		line=each_line.rstrip('\n').split('=')
		api_keys_dict[line[0]] = line[1]

	auth = tweepy.OAuthHandler(api_keys_dict['CONSUMER_KEY'], api_keys_dict['CONSUMER_SECRET'])
	auth.secure = True
	auth.set_access_token(api_keys_dict['ACCESS_KEY'], api_keys_dict['ACCESS_SECRET'])
	api = tweepy.API(auth)
	return api 


		

#1. User flow
#	 run script
#	 look at tweeter
	
#2. To do
#	 define the start text 
#	 make the functions
#	 search tweeter API (i am going to need Use Testing Tool to drive the API)
#	create tweeter account 
#	test tweeter API
#	connect output of markov function to tweeter API


text1 = 'Thanks God it is Friday.'
text2 = 'Oh no it is Monday again.'

# Creating the dictionary for both texts
def make_dict(text):
	text_list = text.split()
	markov_dict = {}
	for i in range(0, len(text_list)-2):
		first_key_word = text_list[i]
		second_word = text_list[i+1]
		third_word = text_list[i+2]
		key = (first_key_word, second_word)
		value_to_append = [third_word]
		old_value = markov_dict.get(key, [])
		new_value = old_value + value_to_append
		markov_dict[key] = new_value
	
	return markov_dict
# print make_dict(text1)


# def make_dict(text):
# 	text_list = text.split()
# 	markov_dict = {}
# 	for i in range(0, len(text_list)-2):
# 		first_key_word = text_list[i]
# 		second_word = text_list[i+1]
# 		third_word = text_list[i+2]
# 		key = (first_key_word, second_word)
# 		value_to_append = [third_word]
# 		old_value = markov_dict.get(key, [])
# 		new_value = old_value + value_to_append
# 		markov_dict[key] = new_value
# 	
# 	return markov_dict
# print make_dict(text2)



# markov chain for rendom text


def new_dict(dict1, dict2):
	
	dict2_keys = dict2.keys()
	for words in dict2_keys:
		old_value = dict1.get(words,[])
		new_value = old_value + dict2[words]
		dict1[words] = new_value
	return dict1
#print new_dict(dict1, dict2)
		

  	

  	
 	
def make_text(unified_dict):
	all_markov_dict_keys = unified_dict.keys()
# 	print unified_dict
 	tuple_key = random.choice(all_markov_dict_keys)
#  	print touple_key
	first_key_word = tuple_key[0]
	second_word = tuple_key[1]
 	markov_text_list = [first_key_word, second_word]
 	max_text_size = 300
 	for i in range(max_text_size):
 		possible_words = unified_dict[tuple_key]
# 		print possible_words 
 		third_word = random.choice(possible_words)
 		if third_word[-1] == '.': 
 			markov_text_list.append(third_word)
 			break
 		markov_text_list.append(third_word)	
# 		print third_word
# 		print markov_text_list
 		tuple_key = (second_word, third_word)
# 		print tuple_key
 		second_word = tuple_key[1]
# 		print second_word
#	print markov_text_list
 	markov_string = " ".join(markov_text_list)
# 	print markov_text_list
#  	print markov_string
 	return markov_string

#print make_text(unified_dict)

api=read_api_keys() 
	
		
dict1 = make_dict(text1)
dict2 = make_dict(text2)
		
unified_dict = new_dict(dict1,dict2)		
		
api.update_status(status=make_text(unified_dict))


	

	
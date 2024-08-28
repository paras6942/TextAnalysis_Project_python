# This program implements Text analysis. 
# Text analysis, also known as text mining or text analytics, refers to
# the process of extracting meaningful information and insights from textual data.

# Define a string/text
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor.diam et labore? et diam magna. et diam amet. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Define the class and its attributes; Implement a code to find frequency of different words in the text.

# Let's create a class called TextAnalyzer to analyze text.

class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText


    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split()
        # Create dictionary
        freqMap = {}

        for word in wordList:
            freqMap[word] = wordList.count(word)

        return freqMap
        
           
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            count = freqDict[word]
            return count
        else:
            return 0
            
            
# Now we will call the functions created above, allowing the functions to execute and generate output.

# Create an object/instance of the TextAnalyzer class
analyzed = TextAnalyzer(givenstring)

# Call the function which converts the data into lower case
print("Formatted Text:", analyzed.fmtText)

# Call the function that prints the frequency of all different words in the text.
freq = analyzed.freqAll()
print(freq)

# Call the function for finding the frequency of a particular word in the text.
word = 'lorem'
count = analyzed.freqOf(word)
print('The word lorem appears %d times in the text. ' % count)

# This is the end of this document.
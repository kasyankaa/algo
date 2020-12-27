
def KMPAlgorythm(pattern, text):
    length_of_pattern = len(pattern)
    length_of_text = len(text)
    num_of_matches=0

    # creating lps[] that will hold the longest prefix suffix
    lps = [0] * length_of_pattern
    pattern_index = 0


    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pattern, length_of_pattern, lps)

    text_index = 0
    while text_index < length_of_text:
        #searching for match
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1

        #finding full match
        if pattern_index == length_of_pattern:
            found=[(text_index - pattern_index),(text_index-1)]
            # print(found)
            pattern_index = lps[pattern_index - 1]
            num_of_matches+=1

        #case of mismatch
        elif text_index < length_of_text and pattern[pattern_index] != text[text_index]:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1
    if num_of_matches == 0:
        return 0
    else:
      return found;



def computeLPSArray(pattern, length_of_pattern, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # always 0
    i = 1
    # the loop calculates lps[i] for i = 1 to length-1
    while i < length_of_pattern:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
                print (len)
            else:
                lps[i] = 0
                i += 1



# text = "asasasfsgsa"
# pattern = "88"
# KMPAlgorythm(pattern, text)
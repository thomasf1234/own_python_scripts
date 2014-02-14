import worker, os

class ColourAdder(worker.Worker):
    
    COLOUR_FILE_PATH = "/home/ad/own_python_scripts/terminal_colours.txt"
    LOCK_FILE_PATH = "/home/ad/own_python_scripts/colour_adder_lockfile.lock"
    type_dict = {
                 'BOLD' : '$(tput bold)',
                 'UNDERLINE' : '$(tput sgr 0 1)'
                 'RESET' : '$(tput sgr0)''
                 }
    colours_dict = None
    
    previous_string = None
    current_string = None
    

    def __init__(self):
        self.__check_for_file(self.COLOUR_FILE_PATH)
        self.retrieve_colours(self.COLOUR_FILE_PATH)
        
    def retrieve_colours(self, file_path)
        file = open(file_path, "r+")
        file_contents = file.read()
        file.close()
        self.colours_dict = self.__create_dictionary(file_contents)
        
    def __create_dictionary(self, file_contents):
        dict = {}
        dictionary_elements_array = file_contents[:-1].split('\n')
        for e in dictionary_elements_array:
            key_val_array = e.split(':')
            dict[key_val_array[0].strip()] = key_val_array[1].strip()
        return dict
        
    def __check_for_file(self, file_path):
        if os.path.exists(file_path):
            pass
        else:
            raise Exception("'%s', file not found!" % file_path)
    
    def add_colours_to_string(self, string):
        list_chars = list(string)
        for i, val in enumerate(list_chars):
            if val == 'F':
                list_chars[i] = colours_dict['RED']+val+type_dict['RESET']
            elif val == '.':
                list_chars[i] = colours_dict['GREEN']+val+type_dict['RESET']
        return ''.join(list_chars)
      
     '''  
     def write_to_screen(self, string):
     #must print only the difference
     #self.current_string = self.add_colours_to_string(file_contents)   
         os.system('print %s' % self.difference_to_print(self.previous_string, self.current_string)))    
        
     def difference_to_print(self, previous, current):
         pass
     
         
     def perform(self):
         
         if check_if_file_updated == True:
             while lockfile_exists == True:
                 wait
             create_lockfile
             read_from_it #sets previous_string to current_string and then updates current_string
             destroy_lockfile
             add_colours_to_string(current_string)
             write_to_screen
         else:
             exit_method
      '''   
         
          
#
    
     

        
        

#colours = {
#            'RED' : '$(tput setaf 1)',
#            'GREEN' : '$(tput setaf 2)'
#            }



#cmd = "cd %s; git diff %s &" % (file_path, file_name)
#os.system(cmd)

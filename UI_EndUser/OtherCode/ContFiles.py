

class ContFile():
    #
    # self.file_handle
    def __init__(file):
        self.open_file(file)
    
    def open_file(file):

        with open(file, 'r') as file_handle:
            for line in file_handle:
                self.
    
    def load_file(scene, file=None):
        if file != None:
            self.open_file(file)




with open (save_path + name_for_files + '.cont', 'a') as file:
    file.write(USER_PROMPT)

for match in matches:
    coords, scale_size = re.findall(pattern_coords, match)
    coords.replace(" ", "")
    scale_size.replace(" ", "")
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    dateStr = str(now)
    with open(save_path + name_for_files + ".cont", 'a') as file:
        file.write(dateStr)
        file.write(',' + coords)
        file.write(',' + scale_size)
        file.write('\n')
    with open(save_path + dateStr + ".txt", 'w') as file:
        file.write(match)   
    url = image_prompt_url(text_prompt=match)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path + dateStr +".png", 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
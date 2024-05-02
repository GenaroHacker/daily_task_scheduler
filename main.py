from src.director import Director

if __name__ == '__main__':
    director = Director()
    director.clear()
    director.sleep(seconds=0.1)
    director.play_sound()
    director.run_script('example.sh')
    director.open_webpage("http://example.com")
    director.execute_command('ls')
    director.start_new_project('Sample Project', 'Initial Setup')
    director.make_progress('Sample Project')

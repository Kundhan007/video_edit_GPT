from driver.video_editing import extract_video, clip_video_front, combine_video_audio, clip_audio_front


def make_driver_functions():
    function_dict = {
        'extract_video': extract_video,
        'clip_video_front': clip_video_front,
        'combine_video_audio': combine_video_audio,
        'clip_audio_front': clip_audio_front,
    }
    return function_dict


def make_last_variable_result(json_structure: list):
    last_function_call = json_structure[-1]
    last_function_call['output_variable_name'] = 'result'


def algorithm_result(json_structure: list):
    make_last_variable_result(json_structure)
    function_dict = make_driver_functions()
    result = ''  # result will be one of the dynamic variables
    for step in json_structure:
        function_name = step["function_name"]
        input_params = step["input_parameters"]
        output_var_name = step["output_variable_name"]

        # Call the function dynamically using the dictionary
        globals()[output_var_name] = function_dict[function_name](**input_params)

    return result

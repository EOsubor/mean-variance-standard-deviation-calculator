import numpy as np

def calculate(list):
  if len(list) == 9:
    calculations = {}
    input_array = np.array(list).reshape((3,3))

    mean_axis0 = np.mean(input_array, axis=0).tolist()
    mean_axis1 = np.mean(input_array, axis=1).tolist()
    mean_flattened = np.mean(input_array)


    variance_axis0 = np.var(input_array, axis=0).tolist()
    variance_axis1 = np.var(input_array, axis=1).tolist()
    variance_flattened = np.var(input_array)
    
    
    std_axis0 = np.std(input_array, axis=0).tolist()
    std_axis1 = np.std(input_array, axis=1).tolist()
    std_flattened = np.std(input_array)


    max_axis0 = np.max(input_array, axis=0).tolist()
    max_axis1 = np.max(input_array, axis=1).tolist()
    max_flattened = np.max(input_array)


    min_axis0 = np.min(input_array, axis=0).tolist()
    min_axis1 = np.min(input_array, axis=1).tolist()
    min_flattened = np.min(input_array)


    sum_axis0 = np.sum(input_array, axis=0).tolist()
    sum_axis1 = np.sum(input_array, axis=1).tolist()
    sum_flattened = np.sum(input_array)

    #axis_array = [mean_axis0, mean_axis1, variance_axis0, variance_axis1, std_axis0, std_axis1, max_axis0, max_axis1, min_axis0, min_axis1, sum_axis0, sum_axis1]
    #for x in axis_array:
      #x = x.tolist()


    calculations['mean'] = [mean_axis0, mean_axis1, mean_flattened]
    calculations['variance'] = [variance_axis0, variance_axis1, variance_flattened]
    calculations['standard deviation'] = [std_axis0, std_axis1, std_flattened]
    calculations['max'] = [max_axis0, max_axis1, max_flattened]
    calculations['min'] = [min_axis0, min_axis1, min_flattened]
    calculations['sum'] = [sum_axis0, sum_axis1, sum_flattened]

  else:
    raise ValueError("List must contain nine numbers.")


  return calculations




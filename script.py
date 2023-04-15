import os
import requests

def main():
    directory = 'securimage-data'
    filenames = os.listdir(directory)
    
    correct_predictions = 0
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        with open(file_path, "rb") as f:
            payload = {'file': f}
            res = requests.post('http://localhost:5002/process', files=payload)

            if res.ok:
                result = res.json()
                pred = result['data']
                actual = filename[:6]

                # print(pred, actual, pred == actual)
                if pred == actual:
                    correct_predictions += 1
            else:
                print('error')

    print(correct_predictions/len(filenames))

if __name__ == "__main__":
    main()
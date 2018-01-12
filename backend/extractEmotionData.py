import json, http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import operator


def getEmotions():
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '9d31238e43f447339619896c0c32c9b9',
    }

    params = urllib.parse.urlencode({
    })

    # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': 'http://blog.yonkausa.com/wp-content/uploads/2015/03/happy-woman.jpg' }"

    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
        #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        jsonDATA = json.loads(data)
        emotions = jsonDATA[0]['scores']
        for emotion in emotions:
            print(emotion)
            print(emotions[emotion])
        sortedEmotions = sorted(emotions.items(), key = operator.itemgetter(1))
        print(sortedEmotions)
        # print(string)
        # print(data)
        print(type(sortedEmotions))
        topThreeEmotions = []
        for i in range(len(sortedEmotions)-3, len(sortedEmotions)):
            topThreeEmotions.append(sortedEmotions[i])
        return topThreeEmotions
        conn.close()
    except Exception as e:
        print(e.args)

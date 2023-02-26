/**

*/
package sdk.model.transform;

import java.math.*;

import javax.annotation.Generated;

import sdk.model.*;
import com.amazonaws.transform.SimpleTypeJsonUnmarshallers.*;
import com.amazonaws.transform.*;

import com.fasterxml.jackson.core.JsonToken;
import static com.fasterxml.jackson.core.JsonToken.*;

/**
 * SendMessageResult JSON Unmarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class SendMessageResultJsonUnmarshaller implements Unmarshaller<SendMessageResult, JsonUnmarshallerContext> {

    public SendMessageResult unmarshall(JsonUnmarshallerContext context) throws Exception {
        SendMessageResult sendMessageResult = new SendMessageResult();

        int originalDepth = context.getCurrentDepth();
        String currentParentElement = context.getCurrentParentElement();
        int targetDepth = originalDepth + 1;

        JsonToken token = context.getCurrentToken();
        if (token == null)
            token = context.nextToken();
        if (token == VALUE_NULL) {
            return sendMessageResult;
        }

        while (true) {
            if (token == null)
                break;

            sendMessageResult.setBotResponse(BotResponseJsonUnmarshaller.getInstance().unmarshall(context));
            token = context.nextToken();
        }

        return sendMessageResult;
    }

    private static SendMessageResultJsonUnmarshaller instance;

    public static SendMessageResultJsonUnmarshaller getInstance() {
        if (instance == null)
            instance = new SendMessageResultJsonUnmarshaller();
        return instance;
    }
}

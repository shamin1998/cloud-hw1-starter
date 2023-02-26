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
 * BotResponse JSON Unmarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class BotResponseJsonUnmarshaller implements Unmarshaller<BotResponse, JsonUnmarshallerContext> {

    public BotResponse unmarshall(JsonUnmarshallerContext context) throws Exception {
        BotResponse botResponse = new BotResponse();

        int originalDepth = context.getCurrentDepth();
        String currentParentElement = context.getCurrentParentElement();
        int targetDepth = originalDepth + 1;

        JsonToken token = context.getCurrentToken();
        if (token == null)
            token = context.nextToken();
        if (token == VALUE_NULL) {
            return null;
        }

        while (true) {
            if (token == null)
                break;

            if (token == FIELD_NAME || token == START_OBJECT) {
                if (context.testExpression("messages", targetDepth)) {
                    context.nextToken();
                    botResponse.setMessages(new ListUnmarshaller<Message>(MessageJsonUnmarshaller.getInstance())

                    .unmarshall(context));
                }
            } else if (token == END_ARRAY || token == END_OBJECT) {
                if (context.getLastParsedParentElement() == null || context.getLastParsedParentElement().equals(currentParentElement)) {
                    if (context.getCurrentDepth() <= originalDepth)
                        break;
                }
            }
            token = context.nextToken();
        }

        return botResponse;
    }

    private static BotResponseJsonUnmarshaller instance;

    public static BotResponseJsonUnmarshaller getInstance() {
        if (instance == null)
            instance = new BotResponseJsonUnmarshaller();
        return instance;
    }
}

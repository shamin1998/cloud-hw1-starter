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
 * BotRequest JSON Unmarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class BotRequestJsonUnmarshaller implements Unmarshaller<BotRequest, JsonUnmarshallerContext> {

    public BotRequest unmarshall(JsonUnmarshallerContext context) throws Exception {
        BotRequest botRequest = new BotRequest();

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
                    botRequest.setMessages(new ListUnmarshaller<Message>(MessageJsonUnmarshaller.getInstance())

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

        return botRequest;
    }

    private static BotRequestJsonUnmarshaller instance;

    public static BotRequestJsonUnmarshaller getInstance() {
        if (instance == null)
            instance = new BotRequestJsonUnmarshaller();
        return instance;
    }
}

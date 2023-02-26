/**

*/
package sdk.model.transform;

import javax.annotation.Generated;

import com.amazonaws.SdkClientException;
import sdk.model.*;

import com.amazonaws.protocol.*;
import com.amazonaws.annotation.SdkInternalApi;

/**
 * SendMessageRequestMarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
@SdkInternalApi
public class SendMessageRequestMarshaller {

    private static final MarshallingInfo<StructuredPojo> BOTREQUEST_BINDING = MarshallingInfo.builder(MarshallingType.STRUCTURED)
            .marshallLocation(MarshallLocation.PAYLOAD).isExplicitPayloadMember(true).build();

    private static final SendMessageRequestMarshaller instance = new SendMessageRequestMarshaller();

    public static SendMessageRequestMarshaller getInstance() {
        return instance;
    }

    /**
     * Marshall the given parameter object.
     */
    public void marshall(SendMessageRequest sendMessageRequest, ProtocolMarshaller protocolMarshaller) {

        if (sendMessageRequest == null) {
            throw new SdkClientException("Invalid argument passed to marshall(...)");
        }

        try {
            protocolMarshaller.marshall(sendMessageRequest.getBotRequest(), BOTREQUEST_BINDING);
        } catch (Exception e) {
            throw new SdkClientException("Unable to marshall request to JSON: " + e.getMessage(), e);
        }
    }

}

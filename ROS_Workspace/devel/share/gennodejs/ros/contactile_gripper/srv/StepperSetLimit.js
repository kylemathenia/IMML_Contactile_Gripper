// Auto-generated. Do not edit!

// (in-package contactile_gripper.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class StepperSetLimitRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.switch = null;
      this.action = null;
    }
    else {
      if (initObj.hasOwnProperty('switch')) {
        this.switch = initObj.switch
      }
      else {
        this.switch = '';
      }
      if (initObj.hasOwnProperty('action')) {
        this.action = initObj.action
      }
      else {
        this.action = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StepperSetLimitRequest
    // Serialize message field [switch]
    bufferOffset = _serializer.string(obj.switch, buffer, bufferOffset);
    // Serialize message field [action]
    bufferOffset = _serializer.string(obj.action, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StepperSetLimitRequest
    let len;
    let data = new StepperSetLimitRequest(null);
    // Deserialize message field [switch]
    data.switch = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [action]
    data.action = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.switch.length;
    length += object.action.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/StepperSetLimitRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4c5c278c9ea572e11c6039a02c19e5a9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string switch
    string action
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StepperSetLimitRequest(null);
    if (msg.switch !== undefined) {
      resolved.switch = msg.switch;
    }
    else {
      resolved.switch = ''
    }

    if (msg.action !== undefined) {
      resolved.action = msg.action;
    }
    else {
      resolved.action = ''
    }

    return resolved;
    }
};

class StepperSetLimitResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.response = null;
    }
    else {
      if (initObj.hasOwnProperty('response')) {
        this.response = initObj.response
      }
      else {
        this.response = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StepperSetLimitResponse
    // Serialize message field [response]
    bufferOffset = _serializer.int64(obj.response, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StepperSetLimitResponse
    let len;
    let data = new StepperSetLimitResponse(null);
    // Deserialize message field [response]
    data.response = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/StepperSetLimitResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4bf37bc717f68787645077428bea3751';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 response
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StepperSetLimitResponse(null);
    if (msg.response !== undefined) {
      resolved.response = msg.response;
    }
    else {
      resolved.response = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: StepperSetLimitRequest,
  Response: StepperSetLimitResponse,
  md5sum() { return '5b0187267379b2af4b8e7118fa12084a'; },
  datatype() { return 'contactile_gripper/StepperSetLimit'; }
};

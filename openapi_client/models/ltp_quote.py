# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class LTPQuote(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentName': 'str',
        'instrumentToken': 'int',
        'lastPrice': 'float'
    }

    attribute_map = {
        'instrumentName': 'instrumentName',
        'instrumentToken': 'instrumentToken',
        'lastPrice': 'lastPrice'
    }

    def __init__(self, instrumentName=None, instrumentToken=None, lastPrice=None, local_vars_configuration=None):  # noqa: E501
        """LTPQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentName = None
        self._instrumentToken = None
        self._lastPrice = None
        self.discriminator = None

        if instrumentName is not None:
            self.instrumentName = instrumentName
        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if lastPrice is not None:
            self.lastPrice = lastPrice

    @property
    def instrumentName(self):
        """Gets the instrumentName of this LTPQuote.  # noqa: E501

        Name of the instrument  # noqa: E501

        :return: The instrumentName of this LTPQuote.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this LTPQuote.

        Name of the instrument  # noqa: E501

        :param instrumentName: The instrumentName of this LTPQuote.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this LTPQuote.  # noqa: E501


        :return: The instrumentToken of this LTPQuote.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this LTPQuote.


        :param instrumentToken: The instrumentToken of this LTPQuote.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def lastPrice(self):
        """Gets the lastPrice of this LTPQuote.  # noqa: E501


        :return: The lastPrice of this LTPQuote.  # noqa: E501
        :rtype: float
        """
        return self._lastPrice

    @lastPrice.setter
    def lastPrice(self, lastPrice):
        """Sets the lastPrice of this LTPQuote.


        :param lastPrice: The lastPrice of this LTPQuote.  # noqa: E501
        :type lastPrice: float
        """

        self._lastPrice = lastPrice

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LTPQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LTPQuote):
            return True

        return self.to_dict() != other.to_dict()
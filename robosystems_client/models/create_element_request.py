from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_element_request_balance_type import CreateElementRequestBalanceType
from ..models.create_element_request_classification import (
  CreateElementRequestClassification,
)
from ..models.create_element_request_element_type import CreateElementRequestElementType
from ..models.create_element_request_period_type import CreateElementRequestPeriodType
from ..models.create_element_request_source import CreateElementRequestSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateElementRequest")


@_attrs_define
class CreateElementRequest:
  """Create a new Element within a taxonomy. For chart-of-accounts
  taxonomies this is how native accounts are added.

      Attributes:
          taxonomy_id (str):
          name (str):
          classification (CreateElementRequestClassification):
          code (None | str | Unset):
          description (None | str | Unset):
          sub_classification (None | str | Unset):
          balance_type (CreateElementRequestBalanceType | Unset):  Default: CreateElementRequestBalanceType.DEBIT.
          period_type (CreateElementRequestPeriodType | Unset):  Default: CreateElementRequestPeriodType.DURATION.
          element_type (CreateElementRequestElementType | Unset):  Default: CreateElementRequestElementType.CONCEPT.
          is_abstract (bool | Unset):  Default: False.
          is_monetary (bool | Unset):  Default: True.
          parent_id (None | str | Unset):
          source (CreateElementRequestSource | Unset):  Default: CreateElementRequestSource.NATIVE.
          currency (str | Unset):  Default: 'USD'.
          qname (None | str | Unset):
          namespace (None | str | Unset):
          external_id (None | str | Unset):
          external_source (None | str | Unset):
  """

  taxonomy_id: str
  name: str
  classification: CreateElementRequestClassification
  code: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  sub_classification: None | str | Unset = UNSET
  balance_type: CreateElementRequestBalanceType | Unset = (
    CreateElementRequestBalanceType.DEBIT
  )
  period_type: CreateElementRequestPeriodType | Unset = (
    CreateElementRequestPeriodType.DURATION
  )
  element_type: CreateElementRequestElementType | Unset = (
    CreateElementRequestElementType.CONCEPT
  )
  is_abstract: bool | Unset = False
  is_monetary: bool | Unset = True
  parent_id: None | str | Unset = UNSET
  source: CreateElementRequestSource | Unset = CreateElementRequestSource.NATIVE
  currency: str | Unset = "USD"
  qname: None | str | Unset = UNSET
  namespace: None | str | Unset = UNSET
  external_id: None | str | Unset = UNSET
  external_source: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    name = self.name

    classification = self.classification.value

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    sub_classification: None | str | Unset
    if isinstance(self.sub_classification, Unset):
      sub_classification = UNSET
    else:
      sub_classification = self.sub_classification

    balance_type: str | Unset = UNSET
    if not isinstance(self.balance_type, Unset):
      balance_type = self.balance_type.value

    period_type: str | Unset = UNSET
    if not isinstance(self.period_type, Unset):
      period_type = self.period_type.value

    element_type: str | Unset = UNSET
    if not isinstance(self.element_type, Unset):
      element_type = self.element_type.value

    is_abstract = self.is_abstract

    is_monetary = self.is_monetary

    parent_id: None | str | Unset
    if isinstance(self.parent_id, Unset):
      parent_id = UNSET
    else:
      parent_id = self.parent_id

    source: str | Unset = UNSET
    if not isinstance(self.source, Unset):
      source = self.source.value

    currency = self.currency

    qname: None | str | Unset
    if isinstance(self.qname, Unset):
      qname = UNSET
    else:
      qname = self.qname

    namespace: None | str | Unset
    if isinstance(self.namespace, Unset):
      namespace = UNSET
    else:
      namespace = self.namespace

    external_id: None | str | Unset
    if isinstance(self.external_id, Unset):
      external_id = UNSET
    else:
      external_id = self.external_id

    external_source: None | str | Unset
    if isinstance(self.external_source, Unset):
      external_source = UNSET
    else:
      external_source = self.external_source

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
        "name": name,
        "classification": classification,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code
    if description is not UNSET:
      field_dict["description"] = description
    if sub_classification is not UNSET:
      field_dict["sub_classification"] = sub_classification
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if element_type is not UNSET:
      field_dict["element_type"] = element_type
    if is_abstract is not UNSET:
      field_dict["is_abstract"] = is_abstract
    if is_monetary is not UNSET:
      field_dict["is_monetary"] = is_monetary
    if parent_id is not UNSET:
      field_dict["parent_id"] = parent_id
    if source is not UNSET:
      field_dict["source"] = source
    if currency is not UNSET:
      field_dict["currency"] = currency
    if qname is not UNSET:
      field_dict["qname"] = qname
    if namespace is not UNSET:
      field_dict["namespace"] = namespace
    if external_id is not UNSET:
      field_dict["external_id"] = external_id
    if external_source is not UNSET:
      field_dict["external_source"] = external_source

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    name = d.pop("name")

    classification = CreateElementRequestClassification(d.pop("classification"))

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_sub_classification(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sub_classification = _parse_sub_classification(d.pop("sub_classification", UNSET))

    _balance_type = d.pop("balance_type", UNSET)
    balance_type: CreateElementRequestBalanceType | Unset
    if isinstance(_balance_type, Unset):
      balance_type = UNSET
    else:
      balance_type = CreateElementRequestBalanceType(_balance_type)

    _period_type = d.pop("period_type", UNSET)
    period_type: CreateElementRequestPeriodType | Unset
    if isinstance(_period_type, Unset):
      period_type = UNSET
    else:
      period_type = CreateElementRequestPeriodType(_period_type)

    _element_type = d.pop("element_type", UNSET)
    element_type: CreateElementRequestElementType | Unset
    if isinstance(_element_type, Unset):
      element_type = UNSET
    else:
      element_type = CreateElementRequestElementType(_element_type)

    is_abstract = d.pop("is_abstract", UNSET)

    is_monetary = d.pop("is_monetary", UNSET)

    def _parse_parent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

    _source = d.pop("source", UNSET)
    source: CreateElementRequestSource | Unset
    if isinstance(_source, Unset):
      source = UNSET
    else:
      source = CreateElementRequestSource(_source)

    currency = d.pop("currency", UNSET)

    def _parse_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    qname = _parse_qname(d.pop("qname", UNSET))

    def _parse_namespace(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    namespace = _parse_namespace(d.pop("namespace", UNSET))

    def _parse_external_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_id = _parse_external_id(d.pop("external_id", UNSET))

    def _parse_external_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    external_source = _parse_external_source(d.pop("external_source", UNSET))

    create_element_request = cls(
      taxonomy_id=taxonomy_id,
      name=name,
      classification=classification,
      code=code,
      description=description,
      sub_classification=sub_classification,
      balance_type=balance_type,
      period_type=period_type,
      element_type=element_type,
      is_abstract=is_abstract,
      is_monetary=is_monetary,
      parent_id=parent_id,
      source=source,
      currency=currency,
      qname=qname,
      namespace=namespace,
      external_id=external_id,
      external_source=external_source,
    )

    create_element_request.additional_properties = d
    return create_element_request

  @property
  def additional_keys(self) -> list[str]:
    return list(self.additional_properties.keys())

  def __getitem__(self, key: str) -> Any:
    return self.additional_properties[key]

  def __setitem__(self, key: str, value: Any) -> None:
    self.additional_properties[key] = value

  def __delitem__(self, key: str) -> None:
    del self.additional_properties[key]

  def __contains__(self, key: str) -> bool:
    return key in self.additional_properties

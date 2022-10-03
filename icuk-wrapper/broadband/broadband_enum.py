# icuk/broadband - enums

from enum import Enum


class broadband_appointment_type(Enum):
  """
  Represents broadband engineer appointment type.
  """
  none = 0
  morning = 1
  afternoon = 2


class broadband_availabity_bridge_tap(Enum):
  """
  Represents broadband availability bridge tap types.
  """
  unknown = 0
  yes = 1
  no = 2


class broadband_ban_type(Enum):
  """
  Represents broadband ban statues.
  """
  ban = 0
  unban = 1


class broadband_care_level(Enum):
  """
  Represents broadband product care level.
  """
  standard = 1
  enhanced = 2


class broadband_carrier_fault_substatus(Enum):
  """
  Represents BTW broadband sub-statuses
  """
  unknown = 0
  completed = 1
  in_progress = 2
  cancellation_in_progress = 3
  cleared = 4
  raised = 5
  validated = 6
  front_end_closed = 7
  submission_in_progress = 8
  cancelled = 9
  in_rcs_validation = 10
  modify_order_in_progress = 11
  clock_suspended = 12
  timed_out = 13
  waiting_on_supplier = 14
  unsubmitted = 15


class broadband_fault_response_type(Enum):
  """
  Represents a response to a broadband fault question.
  """
  not_checked = 0
  confirmed = 1


class broadband_fault_status(Enum):
  """
  Represents the status of a broadband fault.
  """
  open = 0
  closed = 1


class broadband_fault_substatus(Enum):
  """
  Represents the sub-status of a broadband fault
  """
  new_fault = 0
  waiting_carrier_response = 1
  waiting_customer_response = 2
  engineer_offered = 3
  engineer_booked = 4
  awaiting_engineer_notes = 5
  escalated = 6
  directors_service_office = 7
  waiting_confirmation = 8
  pending_ticket_closure = 9
  investigating_internally = 10
  engineering_work = 11


class broadband_interleaving_type(Enum):
  """
  Represents the broadband interleaving options
  """
  yes = 0
  no = 1
  auto = 2


class broadband_ip4(Enum):
  """
  Represents the status of a IPv4 allocation
  """
  dynamic = 0
  static = 1
  static_routed = 2


class broadband_notification_source(Enum):
  """
  Represents the source of a notification
  """
  unknown = 0
  btw = 1
  ttb = 2
  virgin = 3
  sky = 4


class broadband_notification_state(Enum):
  """
  Represents the state of a notification
  """
  unknown = 0
  initial = 1
  update = 2
  closure = 3
  restoration = 4
  cancelled = 5


class broadband_number_transfer(Enum):
  """
  Represents SoGEA number transfer options
  """
  none = 0
  cease = 1
  port_to_voip_icuk = 2
  port_to_voip = 3


class broadband_order_status(Enum):
  """
  Represents the status of a broadband order.
  """
  received = 1
  processing = 2
  committed = 3
  delayed = 4
  complete = 5
  rejected = 6
  cancelled = 7
  sent = 8
  ceased = 9
  migrated_away = 10
  amended = 11
  issued = 12
  all = 100


class broadband_order_subtype(Enum):
  """
  Represents the subtypes of a broadband order.
  """
  provide_directory_number = 1
  provide_address = 2
  migrate_directory_number = 3
  migrate_address = 4
  migrate_family = 5
  copper_to_fibre = 6
  fibre_to_copper = 7
  sim_provide = 8
  home_move = 9
  modify_traffic_weighting = 10
  modify_advanced_services = 11
  modify_speed = 12
  modify_care = 13
  modify_modified_fault_threshold = 15
  modify_interleaving = 16
  cease = 17
  migrate_away = 18
  cancel = 19
  unknown = 20
  migrate = 21
  unsolicited_cease = 22
  amend = 23
  cease_llu = 24
  cease_wlr = 25


class broadband_order_type(Enum):
  """
  Represents the type of a broadband order
  """
  provide = 1
  migrate = 2
  modify = 3
  cease = 4
  all = 100


class broadband_product_class(Enum):
  """
  Represents the type of ADSL service
  """
  home = 1
  business = 2
  enterprise = 3


class broadband_product_market(Enum):
  """
  Represents the ADSL exchange market type.
  """
  both = 0
  market_b = 1
  market_a = 2


class broadband_product_provider(Enum):
  """
  Represents broadband ADSL product provider.
  """
  wbc_21cn = 1
  wbc_20cn = 3
  cable_and_wireless = 4
  ttb = 5


class broadband_quota_action(Enum):
  """
  Represents the ADSL quota action
  """
  default = 0
  speed_limit = 1
  apply_charge = 2


class broadband_snr_type(Enum):
  """
  TTB - Represents the broadband SNR margin option
  """
  snr_6 = 6
  snr_9 = 9
  snr_12 = 12
  snr_15 = 15


class broadband_stability_type(Enum):
  """
  Represents the stability profile
  """
  standard = 0
  stable = 1
  super_stable = 2


class kbd_bet_equipment(Enum):
  """
  Represents a type of BET equipment.
  """
  unkown = 0
  yes = 1
  no = 2
  dont_know = 3 # What??


class kbd_damaged_equipment(Enum):
  """
  Represents the type of damaged equipment in FTTC KBD.
  """
  unkown = 0
  customer_cpe = 1
  nte = 2
  ont = 3
  wiring = 4


class kbd_pproblem_frequency(Enum):
  """
  Represents the frequency of a problem.
  """
  unknown = 0
  permanent = 1
  intermittent = 2


class kbd_problem_type(Enum):
  """
  Represents the KBD problem type.
  """
  unknown = 0
  connection = 1
  ipv6 = 2
  performance = 5
  damaged_equipment = 6


class kbd_type(Enum):
  """
  Represents the type of KBD
  """
  unknown = 0
  intrusive = 1
  non_intrusive = 2


class scc_voucher_eligibility(Enum):
  """
  Represents SCC voucher eligibility
  """
  ineligible = 0
  eligible = 1
  partial = 2


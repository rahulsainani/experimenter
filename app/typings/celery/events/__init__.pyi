"""
This type stub file was generated by pyright.
"""

from .dispatcher import EventDispatcher
from .event import Event, event_exchange, get_exchange, group_from
from .receiver import EventReceiver

"""Monitoring Event Receiver+Dispatcher.

Events is a stream of messages sent for certain actions occurring
in the worker (and clients if :setting:`task_send_sent_event`
is enabled), used for monitoring purposes.
"""
__all__ = (
    "Event",
    "EventDispatcher",
    "EventReceiver",
    "event_exchange",
    "get_exchange",
    "group_from",
)


#include "eventfilter.h"

#include <QDBusConnection>
#include <QDBusInterface>

EventFilter::EventFilter(DeclarativeView* _parent) : QObject(_parent){
    this->parent = _parent;
}

bool EventFilter::eventFilter(QObject *obj, QEvent *event)
{
   if (event->type() == QEvent::ApplicationDeactivate) {
      return true; // The event is handled
   }
   if (event->type() == QEvent::ApplicationActivate) {
      parent->emitToForeground();
      return true;
   }
   return QObject::eventFilter(obj, event); // Unhandled events are passed to the base class
}

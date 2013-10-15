#ifndef EVENTFILTER_H
#define EVENTFILTER_H

#include <QObject>
#include <QEvent>

#include "declarativeview.h"

class EventFilter : public QObject {

public:
    EventFilter(DeclarativeView* parent);
    bool eventFilter(QObject *obj, QEvent *event);

private:
    DeclarativeView* parent;

};


#endif // EVENTFILTER_H

#include <mchck.h>

#include "usb-serial-loopback.desc.h"

static struct cdc_ctx cdc;
static volatile size_t pending = 0;
static volatile bool ready = true;

static const uint8_t hello[] = "hello world\n";

static void
new_data(uint8_t *data, size_t len)
{
        if (ready) {
                onboard_led(-1);
                ready = false;
                pending += sizeof(hello);
                size_t sent = cdc_write(hello, sizeof(hello), &cdc);
                pending -= sent;
        }
        cdc_read_more(&cdc);
}

static void
data_sent(size_t sent)
{
        if (pending == 0)
                ready = true;
}

void
init_vcdc(int config)
{
        cdc_init(new_data, data_sent, &cdc);
}

void
main(void)
{
        usb_init(&cdc_device);
        sys_yield_for_frogs();
}

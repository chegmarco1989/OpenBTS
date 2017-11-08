/* GSMShare/A51.h */
/*-
 *
 */

#ifndef _OPENBTS_GSMSHARE_A51_H
#define _OPENBTS_GSMSHARE_A51_H

#include <stdio.h>
#include <stdlib.h>

typedef unsigned char byte;
typedef unsigned long word;
typedef word bit;

void A51_GSM(byte *key, int klen, int count, byte *block1, byte *block2);

#endif /* _OPENBTS_GSMSHARE_A51_H */

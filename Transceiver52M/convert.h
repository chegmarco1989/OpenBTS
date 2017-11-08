/* Transceiver52M/convert.h */
/*-
 *
 */

#ifndef _CONVERT_H_
#define _CONVERT_H_

#ifdef __cplusplus
extern "C" {
#endif

void convert_float_short(short *out, float *in, float scale, int len);
void convert_short_float(float *out, short *in, int len);

#ifdef __cplusplus
};
#endif

#endif /* _CONVERT_H_ */

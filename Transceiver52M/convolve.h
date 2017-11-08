/* Transceiver52M/convolve.h */
/*-
 *
 */

#ifndef _CONVOLVE_H_
#define _CONVOLVE_H_

#ifdef __cplusplus
extern "C" {
#endif

void *convolve_h_alloc(int num);

int convolve_real(
	float *x, int x_len, float *h, int h_len, float *y, int y_len, int start, int len, int step, int offset);

int convolve_complex(
	float *x, int x_len, float *h, int h_len, float *y, int y_len, int start, int len, int step, int offset);

int base_convolve_real(
	float *x, int x_len, float *h, int h_len, float *y, int y_len, int start, int len, int step, int offset);

int base_convolve_complex(
	float *x, int x_len, float *h, int h_len, float *y, int y_len, int start, int len, int step, int offset);

#ifdef __cplusplus
};
#endif

#endif /* _CONVOLVE_H_ */

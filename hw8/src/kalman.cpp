#include <iostream>
#include <stdexcept>

#include "hw8/kalman.h"

KalmanFilter::KalmanFilter(
  double dt,
  const Eigen::MatrixXd& A,
  const Eigen::MatrixXd& B,
  const Eigen::MatrixXd& C,
  const Eigen::MatrixXd& Q,
  const Eigen::MatrixXd& R,
  const Eigen::MatrixXd& P)
  : A(A), B(B), C(C), Q(Q), R(R), P0(P),
  m(C.rows()), n(A.rows()), dt(dt), initialized(false),
  I(n, n), x_hat(n), x_hat_new(n) 
{
  I.setIdentity();
}

KalmanFilter::KalmanFilter() {
  
}

//Given inital input parameter
void KalmanFilter::init(double t0, const Eigen::VectorXd& x0) {
  x_hat = x0;
  P = P0;
  this->t0 = t0;
  t = t0;
  initialized = true;
}

//If you don't input any parameter
void KalmanFilter::init() {
  x_hat.setZero();
  P = P0;
  t0 = 0;
  t = t0;
  initialized = true;
}

void KalmanFilter::update(const Eigen::VectorXd& y) {

  if (!initialized)
    throw std::runtime_error("Filter is not initialized!");
  //Please refer the page 20 in week_12 kf ptt.
  //x_hat_new is prediction(x_k)
  //x_hat is correction(x_k-1)

  Eigen::MatrixXd K;
  x_hat_new = A * x_hat_new + B * 2;
  P = A * P * A.transpose() + Q;
  K = P * C.transpose() * (C * P * C.transpose() + R ).inverse();
  x_hat = x_hat + K * (y - C * x_hat );
  P = (I - K * C) * P; 

  t += dt;
}

//If you have change your dynamic matrix A
void KalmanFilter::update(const Eigen::VectorXd& y, double dt, const Eigen::MatrixXd A) {

  this->A = A;
  this->dt = dt;
  update(y);
}

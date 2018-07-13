/*
 * Copyright 2018,
 *
 * Joseph Mirabel
 *
 * LAAS, CNRS
 *
 * This file is part of TIAGOController.
 * TIAGOController is a free software, 
 *
 *
 */

#ifndef _SOT_TIAGOSCHUNK_Controller_H_
#define _SOT_TIAGOSCHUNK_Controller_H_

#include "sot-tiago-controller.hh"
namespace dgsot=dynamicgraph::sot;

class SoTTiagoSchunkController: public SoTTiagoController
{
 public:
  static const std::string LOG_PYTHON_TIAGOSCHUNK;

  SoTTiagoSchunkController();
  virtual ~SoTTiagoSchunkController() {};


 protected:

  virtual void startupPython();
  

};

#endif /* _SOTTiagoController_H_ */

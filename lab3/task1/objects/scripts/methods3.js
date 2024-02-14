let ladder = {
    step: 0,
    up() {
      this.step++;
      return;
    },
    down() {
      this.step--;
      return;
    },
    showStep: function() {
      alert( this.step );
      return;
    }
  };

  
ladder.up().up().down().showStep().down().showStep();
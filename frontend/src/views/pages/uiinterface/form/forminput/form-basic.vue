<template>
  <div class="card">
    <div class="card-header">
      <h5 class="card-title">Basic Examples</h5>
    </div>
    <div class="card-body">
      <b-form action="javascript:;">
        <div class="form-group row">
          <label class="col-form-label col-lg-2">Group Left</label>
          <div class="col-lg-10">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">@</span>
              <b-form-input
                type="text"
                class="form-control"
                placeholder="Username"
                aria-label="Username"
                aria-describedby="basic-addon1"
              ></b-form-input>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-form-label col-lg-2">Group Right</label>
          <div class="col-lg-10">
            <div class="input-group">
              <b-form-input
                type="text"
                class="form-control"
                placeholder="Recipient's username"
                aria-label="Recipient's username"
                aria-describedby="basic-addon2"
              ></b-form-input>
              <span class="input-group-text" id="basic-addon2">@example.com</span>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-form-label col-lg-2">URL Example</label>
          <div class="col-lg-10">
            <div class="input-group">
              <span class="input-group-text">https://</span>
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
        </div>

        <div class="form-group row">
          <label class="col-form-label col-lg-2">Group with Price</label>
          <div class="col-lg-10">
            <div class="input-group">
              <span class="input-group-text">$</span>
              <b-form-input type="text" class="form-control"></b-form-input>
              <span class="input-group-text">.00</span>
            </div>
          </div>
        </div>

        <div class="form-group row mb-0">
          <label class="col-form-label col-lg-2">Group with Price (Left)</label>
          <div class="col-lg-10">
            <div class="input-group">
              <span class="input-group-text">$</span>
              <span class="input-group-text">0.00</span>
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
        </div>
      </b-form>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5 class="card-title">Sizing</h5>
    </div>
    <div class="card-body">
      <b-form action="javascript:;">
        <div class="form-group row">
          <label class="col-form-label col-lg-2">Input Group Large</label>
          <div class="col-lg-10">
            <div class="input-group input-group-lg">
              <span class="input-group-text" id="sizing-addon1">@</span>
              <b-form-input
                type="text"
                class="form-control input-height"
                placeholder="Username"
                aria-describedby="sizing-addon1"
              ></b-form-input>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-form-label col-lg-2">Input Group Default</label>
          <div class="col-lg-10">
            <div class="input-group">
              <span class="input-group-text" id="sizing-addon2">@</span>
              <b-form-input
                type="text"
                class="form-control"
                placeholder="Username"
                aria-describedby="sizing-addon2"
              ></b-form-input>
            </div>
          </div>
        </div>
        <div class="form-group row mb-0">
          <label class="col-form-label col-lg-2">Input Group Small</label>
          <div class="col-lg-10">
            <div class="input-group input-group-sm">
              <span class="input-group-text" id="sizing-addon3">@</span>
              <b-form-input
                type="text"
                class="form-control"
                placeholder="Username"
                aria-describedby="sizing-addon3"
              ></b-form-input>
            </div>
          </div>
        </div>
      </b-form>
    </div>
  </div>
</template>

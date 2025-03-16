<template>
  <div class="card-body card-buttons">
    <b-form action="javascript:;">
      <div class="row">
        <div class="col-xl-6">
          <h5 class="card-title">Personal Details</h5>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">First Name</label>
            <div class="col-lg-9 mb-3">
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">Last Name</label>
            <div class="col-lg-9 mb-3">
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">Password</label>
            <div class="col-lg-9 mb-3">
              <b-form-input type="password" class="form-control"></b-form-input>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">State</label>
            <div class="col-lg-9 mb-3">
              <vue-select :options="state" id="state" placeholder="Select State" />
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">About</label>
            <div class="col-lg-9 mb-3">
              <b-form-textarea
                rows="4"
                max-rows="5"
                class="form-control"
                placeholder="Enter message"
              ></b-form-textarea>
            </div>
          </div>
        </div>
        <div class="col-xl-6">
          <h5 class="card-title">Personal details</h5>
          <div class="row">
            <label class="col-lg-3 col-form-label">Name</label>
            <div class="col-lg-9 mb-3">
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <b-form-input
                      type="text"
                      placeholder="First Name"
                      class="form-control"
                    ></b-form-input>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <b-form-input
                      type="text"
                      placeholder="Last Name"
                      class="form-control"
                    ></b-form-input>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">Email</label>
            <div class="col-lg-9 mb-3">
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">Phone</label>
            <div class="col-lg-9 mb-3">
              <b-form-input type="text" class="form-control"></b-form-input>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-lg-3 col-form-label">Address</label>
            <div class="col-lg-9">
              <b-form-input type="text" class="form-control m-b-20"></b-form-input>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group mb-3">
                    <vue-select
                      :options="state1"
                      id="state1"
                      placeholder="Select Country"
                    />
                  </div>
                  <div class="form-group">
                    <b-form-input
                      type="text"
                      placeholder="ZIP code"
                      class="form-control"
                    ></b-form-input>
                  </div>
                </div>
                <div class="col-md-6 mb-3">
                  <div class="form-group mb-3">
                    <b-form-input
                      type="text"
                      placeholder="State/Province"
                      class="form-control"
                    ></b-form-input>
                  </div>
                  <div class="form-group">
                    <b-form-input
                      type="text"
                      placeholder="City"
                      class="form-control"
                    ></b-form-input>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="text-end">
        <b-button variant="primary">Submit</b-button>
      </div>
    </b-form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      state: ["Select State", "California", "Texas", "Florida"],
      state1: ["Select Country", "USA", "France", "India", "Spain"],
    };
  },
  components: {},
  mounted() {},
};
</script>

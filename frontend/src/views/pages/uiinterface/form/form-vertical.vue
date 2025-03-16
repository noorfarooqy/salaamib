<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Vertical Form</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Basic Form</h5>
            </div>
            <div class="card-body">
              <b-form action="javascript:;">
                <div class="input-block mb-3">
                  <label>First Name</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Last Name</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Email Address</label>
                  <b-form-input type="email" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Username</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Password</label>
                  <b-form-input type="password" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Repeat Password</label>
                  <b-form-input type="password" class="form-control" />
                </div>
                <div class="text-end">
                  <b-button type="submit" variant="primary">Submit</b-button>
                </div>
              </b-form>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Address Form</h5>
            </div>
            <div class="card-body">
              <b-form action="javascript:;">
                <div class="input-block mb-3">
                  <label>Address Line 1</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Address Line 2</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>City</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>State</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Country</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="input-block mb-3">
                  <label>Postal Code</label>
                  <b-form-input type="text" class="form-control" />
                </div>
                <div class="text-end">
                  <b-button type="submit" variant="primary">Submit</b-button>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Two Column Vertical Form</h5>
            </div>
            <div class="card-body">
              <b-form action="javascript:;">
                <h5 class="card-title">Personal Information</h5>
                <div class="row">
                  <div class="col-md-6">
                    <div class="input-block mb-3">
                      <label>First Name</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Last Name</label>
                      <input type="text" class="form-control">
                    </div>
                    <div class="input-block mb-3">
                      <label>Blood Group</label>
                      <vue-select :options="bloodgroup" id="bloodgroup" placeholder="Select" />
                    </div>
                    <div class="input-block mb-3">
                      <label class="d-block">Gender:</label>
                      <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="gender" id="gender_male" value="option1">
                        <label class="form-check-label" for="gender_male">Male</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="gender" id="gender_female" value="option2">
                        <label class="form-check-label" for="gender_female">Female</label>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="input-block mb-3">
                      <label>Username</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Email</label>
                      <b-form-input type="text" class="form-control" />
                    </div>

                    <div class="input-block mb-3">
                      <label>Password</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Repeat Password</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                  </div>
                </div>
                <h5 class="card-title">Postal Address</h5>
                <div class="row">
                  <div class="col-md-6">
                    <div class="input-block mb-3">
                      <label>Address Line 1</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Address Line 2</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>State</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="input-block mb-3">
                      <label>City</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Country</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Postal Code</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                  </div>
                </div>
                <div class="text-end">
                  <b-button type="submit" variant="primary">Submit</b-button>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Two Column Vertical Form</h5>
            </div>
            <div class="card-body">
              <b-form action="javascript:;">
                <div class="row">
                  <div class="col-md-6">
                    <h5 class="card-title">Personal details</h5>
                    <div class="input-block mb-3">
                      <label>Name:</label>
                      <b-form-input type="text" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Password:</label>
                      <b-form-input type="password" class="form-control" />
                    </div>
                    <div class="input-block mb-3">
                      <label>State:</label>
                      <vue-select :options="state" id="state" placeholder="Select State" />
                    </div>
                    <div class="input-block mb-3">
                      <label>Your Message:</label>
                      <textarea rows="5" cols="5" class="form-control" placeholder="Enter message"></textarea>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <h5 class="card-title">Personal details</h5>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>First Name:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>Last Name:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>Email:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>Phone:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-12">
                        <div class="input-block mb-3">
                          <label>Address line:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>Country:</label>
                          <vue-select :options="country" id="country" placeholder="Select Country" />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>State/Province:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>ZIP code:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="input-block mb-3">
                          <label>City:</label>
                          <b-form-input type="text" class="form-control" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="text-end">
                  <b-button type="submit" variant="primary">Submit</b-button>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      bloodgroup: ["Select", "A+", "O+", "B+", "AB+"],
      state: ["Select State", "California", "Texas", "Florida"],
      country: ["Select Country", "USA", "France", "India", "Spain"],
      title: "Vertical Form",
    };
  },
  components: {},
  mounted() { },
};
</script>